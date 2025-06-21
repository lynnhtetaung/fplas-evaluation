import 'package:flutter/material.dart';

void main(){
	runApp(const MyApp());
}

class MyApp extends StatelessWidget {
	const MyApp({super.key});
    
    @override
    Widget build(BuildContext context) {
    	return MaterialApp(
        	title: 'テキスト表示アプリ',
            home: Scaffold(
            	appBar: AppBar(
                	title: const Text('ホーム画面'),
                ),
                body: const Center(
                	child: Text(
                    	'こんにちは、Flutter!',
                        style: TextStyle(fontSize: 24),
                        ),
                    ),
                ),
            );
    }
}