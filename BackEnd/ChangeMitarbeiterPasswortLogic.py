import os
import pickle
import sys
from PyQt5.QtWidgets import QMessageBox, QWidget
import Wydbid
from Data import Mitarbeiter


def changePasswortFinal(username: str, passwort: str, new_passwort: str, widget: QWidget):
    if username == '' or passwort == '' or new_passwort == '':
        QMessageBox.warning(Wydbid.app.parent(), 'Warnung',
                            'Alle Felder muessen ausgefuellt werden!')
        return

    if not os.path.exists(f'{Wydbid.firmen_location}Mitarbeiter/{username}.wbm'):
        QMessageBox.warning(Wydbid.app.parent(
        ), 'Achtung', 'Der von Ihnen eingegebene Nutzername bzw. Mitarbeiter existiert nicht.')
        return

    mitarbeiter_file = open(
        f'{Wydbid.firmen_location}Mitarbeiter/{username}.wbm', 'rb')
    mitarbeiter: Mitarbeiter.Mitarbeiter = pickle.load(mitarbeiter_file)
    mitarbeiter_file.close()

    if not mitarbeiter.passwort == passwort:
        QMessageBox.warning(Wydbid.app.parent(), 'Achtung',
                            'Achtung, das eingegebene Passwort ist falsch!')
        return

    mitarbeiter_file_new = open(
        f'{Wydbid.firmen_location}Mitarbeiter/{username}.wbm', 'wb')
    mitarbeiter.passwort = new_passwort
    pickle.dump(mitarbeiter, mitarbeiter_file_new, pickle.HIGHEST_PROTOCOL)

    QMessageBox.about(Wydbid.app.parent(), 'Vorgang abgeschlossen',
                      f'Das Passwort von {username} wurde erfolgreich geändert.')

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
