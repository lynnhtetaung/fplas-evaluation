import 'package:flutter/material.dart';

void main(){
	runApp(MyApp());
}

class MyApp extends StatelessWidget{
	@override
    Widget build(BuildContext context){
    	return MaterialApp(
        	title: 'ElevatedButton Demo',
            home: Scaffold(
            	appBar: AppBar(
                	title: Text('ElevatedButton 表示'),                  
                ),
                body: Center(
                	child: ElevatedButton(
                    	onPressed: (){
                        	print('ボタンが押されました');
                        },
                        child: Text('押す'),
                    ),
                ),
            ),
        );
    }
}