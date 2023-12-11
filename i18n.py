import gettext

class I18N:
    @staticmethod
    def change_locale(locale):
        global _
        locale_path = "./locales"
        translation = gettext.translation('base', locale_path, languages=[locale])
        translation.install()

        _ = translation.gettext