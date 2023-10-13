import 'package:firebase_auth/firebase_auth.dart';
import 'package:firebase_flutter_demo/firebase/forgot_password.dart';
import 'package:firebase_flutter_demo/util/theme_switcher.dart';
import 'package:firebase_flutter_demo/util/utils.dart';
import 'package:flutter/material.dart';
import 'package:flutter/gestures.dart';
import 'package:flutter_svg/flutter_svg.dart';
import 'package:provider/provider.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';

import '../pages/language_picker.dart';
import '../util/logger.util.dart';
import '../main.dart';

class LoginWidget extends StatefulWidget {
  final Function() onClickedSignUp;

  const LoginWidget({
    Key? key,
    required this.onClickedSignUp,
  }) : super(key: key);

  @override
  State<LoginWidget> createState() => _LoginWidgetState();
}

class _LoginWidgetState extends State<LoginWidget> {
  final emailController = TextEditingController();
  final passwordController = TextEditingController();
  final log = getLogger();

  @override
  void dispose() {
    emailController.dispose();
    passwordController.dispose();

    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final themeProvider = Provider.of<ThemeProvider>(context);

    return SingleChildScrollView(
      padding: const EdgeInsets.all(16),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          const SizedBox(
            height: 16,
          ),
          IconButton(
            onPressed: themeProvider.toggleTheme,
            icon: const Icon(Icons.wb_sunny),
          ),
          const SizedBox(
            height: 20,
          ),
          SvgPicture.asset(
            'assets/logo.svg',
            height: 200,
            width: 200,
          ),
          const SizedBox(
            height: 20,
          ),
          const LanguageSelection(),
          const SizedBox(
            height: 40,
          ),
          TextField(
            controller: emailController,
            cursorColor: Colors.white,
            textInputAction: TextInputAction.next,
            decoration: InputDecoration(
              labelText: AppLocalizations.of(context)!.email,
            ),
          ),
          const SizedBox(
            height: 4,
          ),
          TextField(
            controller: passwordController,
            textInputAction: TextInputAction.next,
            decoration: InputDecoration(
              labelText: AppLocalizations.of(context)!.password,
            ),
            obscureText: true,
          ),
          const SizedBox(
            height: 20,
          ),
          ElevatedButton.icon(
            style: ElevatedButton.styleFrom(
              minimumSize: const Size.fromHeight(50),
            ),
            icon: const Icon(
              Icons.lock_open,
              size: 32,
            ),
            label: Text(
              AppLocalizations.of(context)!.log_in,
              style: const TextStyle(
                fontSize: 24,
              ),
            ),
            onPressed: signIn,
          ),
          const SizedBox(
            height: 24,
          ),
          GestureDetector(
            onTap: () => Navigator.of(context).push(
              MaterialPageRoute(
                builder: (context) => const ForgotPasswordPage(),
              ),
            ),
            child: Text(
              AppLocalizations.of(context)!.forgot_password,
              style: TextStyle(
                decoration: TextDecoration.underline,
                color: Theme.of(context).colorScheme.secondary,
                fontSize: 16,
              ),
            ),
          ),
          const SizedBox(
            height: 16,
          ),
          Text.rich(
            TextSpan(
              style: TextStyle(
                color: Theme.of(context).colorScheme.primary,
                fontSize: 16,
              ),
              text: AppLocalizations.of(context)!.no_account,
              children: [
                TextSpan(
                  recognizer: TapGestureRecognizer()
                    ..onTap = widget.onClickedSignUp,
                  text: AppLocalizations.of(context)!.sign_up,
                  style: TextStyle(
                    decoration: TextDecoration.underline,
                    color: Theme.of(context).colorScheme.secondary,
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Future signIn() async {
    showDialog(
      context: context,
      barrierDismissible: false,
      builder: (context) => const Center(
        child: CircularProgressIndicator(),
      ),
    );

    try {
      await FirebaseAuth.instance.signInWithEmailAndPassword(
        email: emailController.text.trim(),
        password: passwordController.text.trim(),
      );
    } on FirebaseAuthException catch (e) {
      log.e(e.message);

      Utils.showSnackBar(e.message);
    }

    navigatorKey.currentState!.popUntil((route) => route.isFirst);
  }
}
