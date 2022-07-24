import os
import pickle
from PyQt5.QtWidgets import QWidget, QMessageBox
import Wydbid
from Data import Mitarbeiter


def delMitarbeiterFinal(username: str, passwort: str, widget: QWidget):
    if username == '' or passwort == '':
        QMessageBox.warning(Wydbid.app.parent(), 'Warnung',
                            'Alle Felder muessen ausgefuellt werden!')
        return

    # See if the file or employee exists
    if not os.path.exists(f'{Wydbid.firmen_location}Mitarbeiter/{username}.wbm'):
        QMessageBox.warning(Wydbid.app.parent(
        ), 'Achtung', 'Der von Ihnen eingegebene Nutzername bzw. Mitarbeiter existiert nicht.')
        return

    readable_file = open(
        f'{Wydbid.firmen_location}Mitarbeiter/{username}.wbm', 'rb')
    file_path = f'{Wydbid.firmen_location}Mitarbeiter/{username}.wbm'

    mitarbeiter: Mitarbeiter.Mitarbeiter = pickle.load(readable_file)
    readable_file.close()

    if not passwort == mitarbeiter.passwort:
        QMessageBox.warning(Wydbid.app.parent(), 'Achtung',
                            'Achtung, das eingegebene Passwort ist falsch!')
        return

    os.remove(file_path)

    QMessageBox.about(Wydbid.app.parent(), 'Abgeschlossen',
                      'Der Mitarbeiter wurde gelöscht!')

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
