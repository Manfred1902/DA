import 'package:firebase_auth/firebase_auth.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_flutter_demo/util/locale_provider.dart';
import 'package:firebase_flutter_demo/util/theme_switcher.dart';
import 'package:firebase_flutter_demo/util/utils.dart';
import 'package:firebase_flutter_demo/firebase/verify_email.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:flutter_native_splash/flutter_native_splash.dart';
import 'package:flutter/material.dart';
import 'package:logger/logger.dart';
import 'package:provider/provider.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';

import 'firebase/auth.dart';
import 'l10n/l10n.dart';

Future main() async {
  WidgetsFlutterBinding.ensureInitialized();
  if (kIsWeb) {
    await Firebase.initializeApp(
      options: const FirebaseOptions(
        apiKey: "AIzaSyBowz9TW7OzskqlDV4OAecVofaOVq9OrO4",
        appId: "1:403469711752:web:643d471e6c19cd869a223d",
        messagingSenderId: "403469711752",
        projectId: "life-in-third-person",
      ),
    );
  } else {
    await Firebase.initializeApp();
  }

  Logger.level = Level.debug;

  WidgetsBinding widgetsBinding = WidgetsFlutterBinding.ensureInitialized();
  FlutterNativeSplash.preserve(widgetsBinding: widgetsBinding);

  runApp(
    MultiProvider(
      providers: [
        ChangeNotifierProvider<ThemeProvider>(
          create: (_) => ThemeProvider(),
        ),
        ChangeNotifierProvider<LocaleProvider>(
          create: (_) => LocaleProvider(),
        ),
      ],
      child: const MyApp(),
    ),
  );

  FlutterNativeSplash.remove();
}

final navigatorKey = GlobalKey<NavigatorState>();

class MyApp extends StatelessWidget {
  static const String title = 'Life in Third-person';

  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return Consumer2<ThemeProvider, LocaleProvider>(
      builder: (context, themeProvider, localeProvider, child) {
        return MaterialApp(
          supportedLocales: L10n.all,
          localizationsDelegates: const [
            AppLocalizations.delegate,
            GlobalMaterialLocalizations.delegate,
            GlobalCupertinoLocalizations.delegate,
            GlobalWidgetsLocalizations.delegate,
          ],
          home: const MainPage(),
          locale: localeProvider.locale,
          scaffoldMessengerKey: Utils.messengerKey,
          navigatorKey: navigatorKey,
          debugShowCheckedModeBanner: false,
          title: title,
          theme: !themeProvider.isDarkMode
              ? ThemeData.dark().copyWith(
                  elevatedButtonTheme: ElevatedButtonThemeData(
                    style: ElevatedButton.styleFrom(
                      foregroundColor: Colors.white,
                      backgroundColor: Colors.blueAccent,
                    ),
                  ),
                  colorScheme: ColorScheme.fromSwatch().copyWith(
                    primaryContainer: Colors.grey,
                    primary: Colors.grey,
                    secondary: Colors.blueAccent,
                  ),
                )
              : ThemeData.light().copyWith(
                  elevatedButtonTheme: ElevatedButtonThemeData(
                    style: ElevatedButton.styleFrom(
                      foregroundColor: Colors.black,
                      backgroundColor: Colors.lightBlueAccent,
                    ),
                  ),
                  colorScheme: ColorScheme.fromSwatch().copyWith(
                    primaryContainer: Colors.black,
                    primary: Colors.black,
                    secondary: Colors.lightBlueAccent,
                  ),
                ),
        );
      },
    );
  }
}

class MainPage extends StatelessWidget {
  const MainPage({super.key});

  @override
  Widget build(BuildContext context) => Scaffold(
        body: StreamBuilder<User?>(
          stream: FirebaseAuth.instance.authStateChanges(),
          builder: (context, snapshot) {
            if (snapshot.hasData) {
              return const VerifyEmailPage();
            } else {
              return const AuthPage();
            }
          },
        ),
      );
}
