import 'package:flutter/material.dart';

void main(){
	runApp(const MyApp());
}

class MyApp extends StatelessWidget{
	const MyApp({super.key});

    @override
    Widget build(BuildContext context){
    	return MaterialApp(
        	title: 'checkbox',
        	home: Scaffold(
        		appBar: AppBar(
                	title: const Text('checkbox'),
                ),
            	body: Center(
            		child: Checkbox(
                        value: true,
                        onChanged: (bool? newValue){
                        },
                    ),
                ),
            ),
        );
    }
}