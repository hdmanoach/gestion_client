from flask import Flask, render_template, request, redirect, url_for
from models import db, Client
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
with app.app_context():
    db.create_all()

# Page d’accueil : liste des clients
@app.route('/')
def index():
    clients = Client.query.all()
    return render_template('index.html', clients=clients)

# Ajouter un client
@app.route('/add', methods=['GET', 'POST'])
#def add_client():
#    if request.method == 'POST':
#       new_client = Client(
#            nom=request.form['nom'],
#            prenom=request.form['prenom'],
#            telephone=request.form['telephone'],
#            email=request.form['email'],
#            boite_postale=request.form['boite_postale'],
#            adresse=request.form['adresse'],
#            ville=request.form['ville'],
#            pays=request.form['pays']
#        )
#        db.session.add(new_client)
#        db.session.commit()
#        return redirect(url_for('index'))
#    return render_template('add_client.html')

@app.route('/add', methods=['GET', 'POST'])
def add_client():
    if request.method == 'POST':
        email = request.form['email']

        # Vérifie si un client existe déjà
        existing_client = Client.query.filter_by(email=email).first()
        if existing_client:
            # On renvoie le template avec un message d’erreur
            return render_template('add_client.html', error="Cet email existe déjà.")

        try:
            new_client = Client(
                nom=request.form['nom'],
                prenom=request.form['prenom'],
                telephone=request.form['telephone'],
                email=email,
                boite_postale=request.form['boite_postale'],
                adresse=request.form['adresse'],
                ville=request.form['ville'],
                pays=request.form['pays']
            )
            db.session.add(new_client)
            db.session.commit()

            # On peut rediriger avec un paramètre GET pour signaler le succès
            return redirect(url_for('add_client', success=1))

        except Exception as e:
            db.session.rollback()
            return render_template('add_client.html', error="Erreur : " + str(e))

    # Afficher le message de succès s’il existe dans l’URL
    success = request.args.get('success')
    return render_template('add_client.html', success=success)

# Modifier un client
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_client(id):
    clientUpdate = Client.query.get_or_404(id)

    if request.method == 'POST':
        new_email = request.form['email']

        # Vérifie si un autre client a déjà cet email
        existing_client = Client.query.filter(
            Client.email == new_email,
            Client.id != id  # exclure le client qu'on modifie
        ).first()

        if existing_client:
            # Rendre le template avec un message d'erreur
            return render_template(
                'edit_client.html',
                client=clientUpdate,
                error="Cet email est déjà utilisé par un autre client."
            )

        # Si tout est bon, mettre à jour les champs
        clientUpdate.nom = request.form['nom']
        clientUpdate.prenom = request.form['prenom']
        clientUpdate.telephone = request.form['telephone']
        clientUpdate.email = new_email
        clientUpdate.boite_postale = request.form['boite_postale']
        clientUpdate.adresse = request.form['adresse']
        clientUpdate.ville = request.form['ville']
        clientUpdate.pays = request.form['pays']

        try:
            db.session.commit()
            # Affiche message de succès avant de rediriger
            return render_template(
                'edit_client.html',
                client=clientUpdate,
                success=True
            )
        except Exception as e:
            db.session.rollback()
            return render_template(
                'edit_client.html',
                client=clientUpdate,
                error="Erreur lors de la mise à jour : " + str(e)
            )

    return render_template('edit_client.html', client=clientUpdate)


# Supprimer un client
@app.route('/delete/<int:id>')
def delete_client(id):
    client = Client.query.get_or_404(id)
    db.session.delete(client)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
