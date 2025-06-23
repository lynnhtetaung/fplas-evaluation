import 'package:flutter/material.dart';

void main(){
	runApp(MyApp());
}

class MyApp extends StatelessWidget{
	@override
    Widget build(BuildContext context){
    	return MaterialApp(
        	title: 'テキストフィールドサンプル',
            home: TextFieldDemo(),
        );
    }
}

class TextFieldDemo extends StatefulWidget{
	@override
    _TextFieldDemoState createState() => _TextFieldDemoState();
}

class _TextFieldDemoState extends State<TextFieldDemo>{
	String _inputText = '';
    final _controller = TextEditingController();
    
    @override
    void dispose(){
    	_controller.dispose();
        super.dispose();
    }
    
    @override
    Widget build(BuildContext context){
    	return Scaffold(
        	appBar: AppBar(
            	title: Text('テキストフィールド表示'),
            ),
            body: Padding(
            	padding: const EdgeInsets.all(16.0),                     
                   	child: Column(
                    	children: [
                        	TextField(
                            	controller: _controller,
                                decoration: InputDecoration(
                                	labelText: 'Enter Name',
                                    border: OutlineInputBorder(),
                                ),
                                onChanged: (text){
                                	setState((){
                                    	_inputText = text;                                    
                                    });                                
                                },
                            ),
                            
                        ],
                    ),
                ),
            );
       
    }
}