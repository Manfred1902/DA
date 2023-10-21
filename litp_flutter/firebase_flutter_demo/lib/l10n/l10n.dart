import 'package:flutter/material.dart';

class L10n {
  static final all = [
    const Locale('en'),
    const Locale('es'),
    const Locale('ru'),
    const Locale('de'),
  ];

  static String getFlag(String code) {
    switch (code) {
      case 'ru':
        return '🇷🇺';
      case 'es':
        return '🇪🇸';
      case 'de':
        return '🇩🇪';
      case 'en':
      default:
        return '🇬🇧';
    }
  }

  static String getCountryName(String code) {
    switch (code) {
      case 'ru':
        return 'Русский';
      case 'es':
        return 'Español';
      case 'de':
        return 'Deutsch';
      case 'en':
      default:
        return 'English';
    }
  }
}
