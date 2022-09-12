import 'package:flutter/material.dart';
import 'package:login/modules/login/login.dart';
import 'package:login/modules/login/signin.dart';
import 'package:login/modules/homebage/Homebage.dart';
import 'package:login/shared/components/constants.dart';
import 'package:login/shared/styles/styles.dart';

import 'package:login/modules/output/output.dart';

void main ()
{
  runApp(MyApp());
}
// 
class MyApp extends StatelessWidget {
  Widget build (BuildContext context)
  {
         return MaterialApp(
      debugShowCheckedModeBanner: false,
      // ignore: prefer_const_constructors
      home: LogIn() 
    );
  }
}