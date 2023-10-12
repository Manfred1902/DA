import 'package:firebase_auth/firebase_auth.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_flutter_demo/util/theme-switcher.dart';
import 'package:firebase_flutter_demo/util/utils.dart';
import 'package:firebase_flutter_demo/firebase/verify_email.dart';
import 'package:flutter_native_splash/flutter_native_splash.dart';
import 'package:flutter/material.dart';
import 'package:logger/logger.dart';
import 'package:provider/provider.dart';

import 'firebase/auth.dart';

Future main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();

  Logger.level = Level.debug;

  WidgetsBinding widgetsBinding = WidgetsFlutterBinding.ensureInitialized();
  FlutterNativeSplash.preserve(widgetsBinding: widgetsBinding);

  runApp(const MyApp());

  FlutterNativeSplash.remove();
}

final navigatorKey = GlobalKey<NavigatorState>();

class MyApp extends StatelessWidget {
  static const String title = 'Life in Third-person';

  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (_) => ThemeProvider(),
      child: Consumer<ThemeProvider>(
        builder: (context, themeProvider, child) {
          return MaterialApp(
            home: const MainPage(),
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
      ),
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
