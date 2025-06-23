import 'package:flutter/material.dart';

void main(){
	runApp(MyApp());
}

class MyApp extends StatelessWidget{
	@override
    Widget build(BuildContext context){
		return MaterialApp(
        	title: 'Sample of TextField',
            home: TextFieldSample(),
        );
    }
}

class TextFieldSample extends StatefulWidget{
	@override
    _TextFieldSampleState createState() => _TextFieldSampleState();
}

class _TextFieldSampleState extends State<TextFieldSample>{
	String _inputText = '';
    
    @override
    Widget build(BuildContext context){
    	return Scaffold(
        	appBar: AppBar(
            	title: Text('Example of TextField'),
            ),
            body: Padding(
            	padding: const EdgeInsets.all(16.0),
                child: Column(
                	children: [
                    	TextField(
                        	decoration: InputDecoration(
                            	labelText: 'Input here.',
                                border: OutlineInputBorder(),
                            ),
                            onChanged: (text){
                            	setState((){
                                _inputText = text;
                                });
                            },
                        ),
                        SizedBox(height: 20),
                        Text(
                        	'Inputted: $_inputText',
                            style: TextStyle(fontSize: 18),
                        ),
                    ],
                ),
            ),
        );
    }
}