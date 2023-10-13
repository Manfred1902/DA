import 'package:firebase_flutter_demo/util/locale_provider.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:firebase_flutter_demo/l10n/l10n.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';

class LanguageSelection extends StatelessWidget {
  const LanguageSelection({super.key});

  @override
  Widget build(BuildContext context) {
    final localeProvider = Provider.of<LocaleProvider>(context);

    return DropdownButtonFormField<Locale>(
      alignment: Alignment.center,
      value: localeProvider.locale,
      onChanged: (Locale? newLocale) {
        if (newLocale != null) {
          localeProvider.setLocale(newLocale);
        }
      },
      items: L10n.all.map(
        (Locale locale) {
          return DropdownMenuItem(
            alignment: Alignment.center,
            value: locale,
            child: Row(
              children: [
                Text(
                  L10n.getFlag(locale.languageCode),
                  textAlign: TextAlign.center,
                ),
                const SizedBox(width: 10),
                Text(
                  L10n.getCountryName(locale.languageCode),
                  textAlign: TextAlign.center,
                ),
              ],
            ),
          );
        },
      ).toList(),
      decoration: InputDecoration(
        labelText: AppLocalizations.of(context)!.select_language,
      ),
      selectedItemBuilder: (BuildContext context) {
        return L10n.all.map(
          (Locale locale) {
            return Text(
              L10n.getCountryName(locale.languageCode),
            );
          },
        ).toList();
      },
      icon: const Icon(Icons.arrow_drop_down),
    );
  }
}
