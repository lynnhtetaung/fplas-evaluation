import 'package:flutter/material.dart';

void main(){
	runApp(const MyApp());
}

class MyApp extends StatelessWidget {
	const MyApp({super.key});
    
    @override
    Widget build(BuildContext context) {
    	return MaterialApp(
        	title:'Eleveted',
            home: Scaffold(
            	appBar: AppBar(
                	title: const Text('Elevatedbutton'),
                ),
                body: Center(
                	child: ElevatedButton(
                    onPressed: () {
                    	print('pushed');
                    },
                    child: const Text('Push'),
                    ),
                ),
            ),
        );
    }


}