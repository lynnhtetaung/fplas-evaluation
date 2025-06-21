import 'package:flutter/material.dart';

void main(){
	runApp(MyApp());
}

class MyApp extends StatefulWidget{
	@override
    State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp>{
	String value = 'A';
    
    @override
    Widget build(BuildContext context){
    	return MaterialApp(
        	home: Scaffold(
	        	body: Center(
		        	child: DropdownButton<String>(
    		        	value: value,
        		        items: ['Apple', 'Grape', 'Banana'].map((e) => DropdownMenuItem(value: e, child: Text(e))).toList(),
            		    onChanged: (val) => setState(() => value = val!),
            		),
            	),
            ),
        );
    }
}