from flask import Blueprint, request, render_template, flash, redirect
from StoreData.controller.FileController import FileController

data = Blueprint('data', __name__)

image = FileController()


@data.route('/save', methods=['POST', 'GET'])
def save():
    if request.method == 'POST':
        try:
            image.saveFile()
            flash('Fichier enregistrée avec succès', 'success')
            return redirect('data.all', 200)
        except Exception as e:
            flash('Fichier non enregistrée', 'error')
            return redirect('data.all',500)
    return render_template('file/index.html')


@data.route('/all')
def all():
    try:
        img = image.getFile()
        flash('Fichier enregistrée avec succès', 'success')
        return render_template('file/index.html', images=img)
    except Exception as e:
        return render_template('file/index.html')


@data.route('/delete/<int:id>')
def delete(id):
    try:
        image.deleteFile(id)
        flash('Fichier supprimée avec succès', 'success')
        return render_template('file/index.html')
    except Exception as e:
        return flash('Fichier non supprimée', 'error')
