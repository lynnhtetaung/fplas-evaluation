import 'package:flutter/material.dart';

void main() {
	runApp(const MyApp());
}

class MyApp extends StatelessWidget {
	const MyApp({super.key});
    
    @override
    Widget build(BuildContext context) {
    	return MaterialApp(
        	title: 'テキストフィールドの例',
            home: Scaffold(
            	appBar: AppBar(
                	title: const Text('入力フォーム'),
                ),
                body: const Padding(
                	padding: EdgeInsets.all(16.0),
                    child: MyTextFieldWidget(),
                ),
            ),
        );
    }
}

class MyTextFieldWidget extends StatefulWidge {
	const MyTextFieldWidget({super.key});
    
    @override
    State<MyTextFieldWidget> create() => _MyTextFieldWidgetState();
}


class _MyTextFieldWidgetState extends State<MyTextFieldWidget>{
	final TextEditingController _controller = TextEditingController();
    
    @override
    void dispose(){
    	_controller.dispose(); //メモリ解放
        super.dispose();
    }
    
    @override
    Widget build(BuildContext context){
    	return Column(
        	children:[
            	TextField(
                	controller: _controller,
                    decoration: const InputDecoration(
                    	labelText: '文字を入力してください',
                        border: OutlineInputBorder(),
                    ),
                ),
                const SizeBox(height: 16),
                ElevatedButton(
                	onPressed: (){
                    	final enteredText = _controller.text;
                        showDialog(
                        	conetxt: context,
                            buildter: (_) => AlertDialog(
                            	content: Text('入力内容: $enteredText'),
                            ),
                        );
                    },
                    child: const Text('表示'),
                ),
            ],
        );
    }
}