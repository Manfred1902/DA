import 'package:email_validator/email_validator.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:firebase_flutter_demo/main.dart';
import 'package:firebase_flutter_demo/util/utils.dart';
import 'package:flutter/gestures.dart';
import 'package:flutter/material.dart';
import 'package:flutter_svg/svg.dart';
import 'package:provider/provider.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';

import '../pages/language_picker.dart';
import '../util/logger.util.dart';
import '../util/theme_switcher.dart';

class SignUpWidget extends StatefulWidget {
  final Function() onClickedSignIn;

  const SignUpWidget({
    Key? key,
    required this.onClickedSignIn,
  }) : super(key: key);

  @override
  State<SignUpWidget> createState() => _SignUpWidgetState();
}

class _SignUpWidgetState extends State<SignUpWidget> {
  final formKey = GlobalKey<FormState>();
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
      child: Form(
        key: formKey,
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
            TextFormField(
              controller: emailController,
              cursorColor: Colors.white,
              textInputAction: TextInputAction.next,
              decoration: InputDecoration(
                labelText: AppLocalizations.of(context)!.email,
              ),
              autovalidateMode: AutovalidateMode.onUserInteraction,
              validator: (email) =>
                  email != null && !EmailValidator.validate(email)
                      ? AppLocalizations.of(context)!.valid_email
                      : null,
            ),
            const SizedBox(
              height: 4,
            ),
            TextFormField(
              controller: passwordController,
              cursorColor: Colors.white,
              textInputAction: TextInputAction.next,
              decoration: InputDecoration(
                labelText: AppLocalizations.of(context)!.password,
              ),
              autovalidateMode: AutovalidateMode.onUserInteraction,
              validator: (value) => value != null && value.length < 6
                  ? AppLocalizations.of(context)!.min_of_six_chars
                  : null,
              obscureText: true,
            ),
            const SizedBox(
              height: 4,
            ),
            TextFormField(
              cursorColor: Colors.white,
              textInputAction: TextInputAction.next,
              decoration: InputDecoration(
                labelText: AppLocalizations.of(context)!.repeat_password,
              ),
              autovalidateMode: AutovalidateMode.onUserInteraction,
              validator: (value) => value != passwordController.text
                  ? AppLocalizations.of(context)!.password_match
                  : null,
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
                Icons.arrow_forward,
                size: 32,
              ),
              label: Text(
                AppLocalizations.of(context)!.sign_up,
                style: const TextStyle(fontSize: 24),
              ),
              onPressed: signUp,
            ),
            const SizedBox(
              height: 20,
            ),
            Text.rich(
              TextSpan(
                style: TextStyle(
                  color: Theme.of(context).colorScheme.primary,
                  fontSize: 16,
                ),
                text: AppLocalizations.of(context)!.already_have_an_account,
                children: [
                  TextSpan(
                    recognizer: TapGestureRecognizer()
                      ..onTap = widget.onClickedSignIn,
                    text: AppLocalizations.of(context)!.log_in,
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
      ),
    );
  }

  Future signUp() async {
    final isValid = formKey.currentState!.validate();
    if (!isValid) return;

    showDialog(
      context: context,
      barrierDismissible: false,
      builder: (context) => const Center(
        child: CircularProgressIndicator(),
      ),
    );

    try {
      await FirebaseAuth.instance.createUserWithEmailAndPassword(
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
