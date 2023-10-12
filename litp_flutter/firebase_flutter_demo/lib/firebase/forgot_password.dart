import 'package:email_validator/email_validator.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:firebase_flutter_demo/util/utils.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../util/logger.util.dart';
import '../util/theme-switcher.dart';

class ForgotPasswordPage extends StatefulWidget {
  const ForgotPasswordPage({super.key});

  @override
  State<ForgotPasswordPage> createState() => _ForgotPasswordPageState();
}

class _ForgotPasswordPageState extends State<ForgotPasswordPage> {
  final formKey = GlobalKey<FormState>();
  final emailController = TextEditingController();
  final log = getLogger();

  @override
  void dispose() {
    emailController.dispose();

    super.dispose();
  }

  @override
  Widget build(BuildContext context) => Scaffold(
        body: Padding(
          padding: const EdgeInsets.all(16),
          child: Form(
            key: formKey,
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const Text(
                  'Receive an email to\nreset your password.',
                  textAlign: TextAlign.center,
                  style: TextStyle(fontSize: 24),
                ),
                const SizedBox(
                  height: 20,
                ),
                TextFormField(
                  controller: emailController,
                  cursorColor: Colors.white,
                  textInputAction: TextInputAction.done,
                  decoration: const InputDecoration(
                    labelText: 'Email',
                  ),
                  autovalidateMode: AutovalidateMode.onUserInteraction,
                  validator: (email) =>
                      email != null && !EmailValidator.validate(email)
                          ? 'Enter a valid email'
                          : null,
                ),
                const SizedBox(
                  height: 20,
                ),
                ElevatedButton.icon(
                  style: ElevatedButton.styleFrom(
                    minimumSize: const Size.fromHeight(50),
                  ),
                  icon: const Icon(
                    Icons.email_outlined,
                    size: 32,
                  ),
                  label: const Text(
                    'Reset Password',
                    style: TextStyle(fontSize: 24),
                  ),
                  onPressed: resetPassword,
                ),
              ],
            ),
          ),
        ),
      );

  Future resetPassword() async {
    showDialog(
      context: context,
      barrierDismissible: false,
      builder: (context) => const Center(
        child: CircularProgressIndicator(),
      ),
    );

    try {
      await FirebaseAuth.instance
          .sendPasswordResetEmail(email: emailController.text.trim());

      Utils.showSnackBar('Password Reset Email Sent');

      // https://stackoverflow.com/questions/68871880/do-not-use-buildcontexts-across-async-gaps
      if (!mounted) return;
      Navigator.of(context).popUntil((route) => route.isFirst);
    } on FirebaseAuthException catch (e) {
      log.e(e.message);

      Utils.showSnackBar(e.message);
      Navigator.of(context).pop();
    }
  }
}
