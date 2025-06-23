import 'package:flutter/material.dart';

void main() => runApp(MaterialApp(home: MyApp()));

class MyApp extends StatefulWidget {
	@override
    State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
	String value = 'Apple';
    
    @override
    Widget build(BuildContext context) {
    	return Scaffold(
        	backgroundColor: Color(0xFFF8F0FF),
            body: Center(
            	child: Container(
                	padding: EdgeInsets.symmetric(horizontal: 12),
                    decoration:BoxDecoration(
                    	border: Border.all(color: Colors.red),
                        borderRadius: BorderRadius.circular(8),
                    ),
                    child: DropdownButtonHideUnderline(
                    	child: DropdownButton(
                        	value: value,
                            items: ['Apple','Banana','Cherry']
                            	.map((e) => DropdownMenuItem(value: e, child: Text(e)))
                                .toList(),
                            onChanged: (v) => setState(() => value = v!),
                        ),
                    ),
                ),
            ),
        );
    }
}