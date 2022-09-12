import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

Widget defultButton({
  Color color = Colors.black,
  required String text,
  bool textUpper = true,
  required VoidCallback func,
  double size = 20,
}) =>
    Container(
      height: 50,
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(20),
        color: color,
      ),
      child: MaterialButton(
        onPressed: func,
        child: Text(
          textUpper ? text.toUpperCase() : text,
          style: TextStyle(
            color: Colors.white,
            fontSize: size,
            fontWeight: FontWeight.bold,
          ),
        ),
      ),
    );

Widget defultFormField({
  required TextEditingController controller,
  required TextInputType type,
  bool isPassword = false,
  required String hintText,
  required IconData prefix,
  IconData? sufix,
  required Function onChange,
  required FormFieldValidator validate,
  VoidCallback? sufixpressed,
}) =>
    TextFormField(
      
      // حتى احسن اوصل للايميل او الباسوورد
      controller: controller,
      keyboardType: type,
      // بحط النقط تبع الباسوورد بأظهر الكلام او يخفيه
      obscureText: isPassword,
      decoration: InputDecoration(
        hintText: hintText,
        prefixIcon: Icon(prefix),
        suffixIcon: sufix != null
            ? IconButton(
                icon: Icon(sufix),
                onPressed: sufixpressed,
              )
            : null,
        border: OutlineInputBorder(
          borderRadius: BorderRadius.all(Radius.circular(50.0)),
        ),
      ),
      validator: validate,
      // بتشتغل لما اكبس عالزر الصح انو خلصت كتابة
      // onFieldSubmitted: (value) {
      //   print(value);
      // },
      // بتشتغل اثناء التعديل على النص فورا
      onChanged: (value) {
        onChange;
      },
    );

Widget viewlist({
  required String valueSeasons,
  ValueChanged? set_State,
  required List<String> listSeasons,
  Color color = Colors.white10,
  // double h = 0,
  // double w = 0 ,
}) =>
    Padding(
      padding: const EdgeInsets.all(8.0),
      child: Container(
          decoration: BoxDecoration(
          
             border: Border.all(color: Colors.black),
                    
            borderRadius: BorderRadius.circular(8),
            color: color,
          ),
          child: DropdownButton(
            value: valueSeasons,
            onChanged: set_State,
            items: listSeasons.map((String items) {
              return DropdownMenuItem(
                value: items,
                child: Text(items),
              );
            }).toList(),
          )),
    );

