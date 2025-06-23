import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Name Input Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const NameInputScreen(),
    );
  }
}

class NameInputScreen extends StatefulWidget {
  const NameInputScreen({super.key});

  @override
  State<NameInputScreen> createState() => _NameInputScreenState();
}

class _NameInputScreenState extends State<NameInputScreen> {
  final TextEditingController _controller = TextEditingController();
  String _enteredName = '';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Enter Your Name')),
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text(
              'Enter name:',
              style: TextStyle(fontSize: 20),
            ),
            const SizedBox(height: 10),
            TextField(
              controller: _controller,
              decoration: const InputDecoration(
                border: OutlineInputBorder(),
                hintText: 'Your name',
              ),
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                setState(() {
                  _enteredName = _controller.text;
                });
              },
              child: const Text('Confirm'),
            ),
            const SizedBox(height: 20),
            Text(
              'Hello, $_enteredName',
              style: const TextStyle(fontSize: 18),
            ),
          ],
        ),
      ),
    );
  }
}