import 'package:flutter/material.dart';

void main() => runApp(MaterialApp(home: Scaffold(body: Center(child: DropdownButton<String>(items: [DropdownMenuItem(value: '1',child: Text('Apple')),DropdownMenuItem(value: '2', child: Text('orange'))], onChanged:(v){})))));