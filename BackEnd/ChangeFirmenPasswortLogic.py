import os
import pickle
from PyQt5.QtWidgets import QComboBox, QMessageBox, QWidget
from Data import Firma
import Wydbid


def addItems(firma_liste: QComboBox):
    l = f'{Wydbid.location}Firmen/'
    files = []

    for folder in os.listdir(l):
        for file in os.listdir(l + folder):
            if file.endswith('.wbf'):
                files.append(f'{l}{folder}/{file}')

    for n_file in files:
        try:
            n = open(n_file, 'rb')
        except:
            QMessageBox.about(Wydbid.app.parent(), 'Warnung',
                              'Etwas ist schiefgelaufen!')
            return

        try:
            firma: Firma.Firma = pickle.load(n)
        except:
            QMessageBox.about(Wydbid.app.parent(), 'Warnung',
                              'Etwas ist schiefgelaufen!')
            return

        firma_liste.addItem(firma.name, [firma, n_file])


def changePasswortFinal(firma_box: QComboBox, old_passwort: str, new_passwort: str, widget: QWidget):
    if firma_box.currentData() == None or new_passwort == '' or old_passwort == '':
        QMessageBox.warning(Wydbid.app.parent(), 'Warnung',
                            'Alle Felder muessen ausgefuellt werden!')
        return

    firma: Firma.Firma = firma_box.currentData()[0]
    if old_passwort == firma.passwort:
        firma.passwort = new_passwort
        writer = open(firma_box.currentData()[1], 'wb')
        pickle.dump(firma, writer, pickle.HIGHEST_PROTOCOL)
        writer.close()

        QMessageBox.about(Wydbid.app.parent(), 'Vorgang abgeschlossen',
                          f'Das Passwort von {firma.name} wurde erfolgreich geändert.')

        m = QMessageBox.question(Wydbid.app.parent(),
                                 'Wydbid neustarten',
                                 'Achtung, um die Änderungen auszuführen, müssen Sie Wydbid neustarten! Wollen Sie jetzt neustarten?',
                                 QMessageBox.Yes,
                                 QMessageBox.No)

        if m == QMessageBox.No:
            widget.close()
            return

        elif m == QMessageBox.Yes:
            Wydbid.app.exit(0)
    else:
        QMessageBox.warning(Wydbid.app.parent(), 'Achtung',
                            'Das eingegebene Passwort ist falsch!')
        return
