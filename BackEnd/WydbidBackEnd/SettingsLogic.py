import pickle
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
import Wydbid
from Data import Settings


def loadCurrentSettingsToPrefab(settings):
    try:
        file = open(f'{Wydbid.location}settings.wbs', 'rb')
        _settings: Settings.Settings = pickle.load(file)

        applySettingsPreSure(_settings=_settings, settings=settings)
    except:
        settings.icon.setText('./Assets/Icon.jpeg')
        settings.mode.setCurrentIndex(1)


def applySettingsPreSure(_settings: Settings.Settings, settings):
    settings.icon.setText(_settings.iconpath)

    if _settings.mode == 'light':
        settings.mode.setCurrentIndex(0)
    elif _settings.mode == 'dark':
        settings.mode.setCurrentIndex(1)


def saveAndApplySetttings(settings):
    icon_path = settings.icon.text()
    mode = settings.mode.currentData()

    # Apply settings

    if mode == 'light':
        Wydbid.app.setStyleSheet('')
    elif mode == 'dark':
        stylesheet = open('./Assets/stylesheet', 'r').read()
        Wydbid.app.setStyleSheet(stylesheet)

    Wydbid.app.setWindowIcon(QIcon(icon_path))

    # Save settings

    _settings = Settings.Settings(iconpath=icon_path, mode=mode)
    file = open(f'{Wydbid.location}settings.wbs', 'wb')

    pickle.dump(_settings, file, pickle.HIGHEST_PROTOCOL)

    QMessageBox.about(Wydbid.app.parent(), 'Process completed',
                      'Changes applied.')

    settings.hide()


def loadSettings():
    try:
        file = open(f'{Wydbid.location}settings.wbs', 'rb')
        _settings: Settings.Settings = pickle.load(file)
    except:
        return

    applySettings(settings=_settings)


def applySettings(settings: Settings.Settings):
    icon_path = settings.iconpath
    mode = settings.mode

    # Apply settings

    if mode == 'light':
        Wydbid.app.setStyleSheet('')
    elif mode == 'dark':
        stylesheet = open('./Assets/stylesheet', 'r').read()
        Wydbid.app.setStyleSheet(stylesheet)

    Wydbid.app.setWindowIcon(QIcon(icon_path))
