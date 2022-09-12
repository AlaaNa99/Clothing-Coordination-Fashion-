import 'package:dio/dio.dart';
import 'package:flutter/material.dart';
import 'package:login/url.dart';
import 'package:shared_preferences/shared_preferences.dart';

class OutPutSecond extends StatefulWidget {
  const OutPutSecond({Key? key}) : super(key: key);

  @override
  State<OutPutSecond> createState() => _OutPutSecondState();
}

class _OutPutSecondState extends State<OutPutSecond> with SingleTickerProviderStateMixin {
  // late AnimationController _controller;

  // @override
  // void initState() {
  //   super.initState();
  //   _controller = AnimationController(vsync: this);
  // }
List<Widget> listImage = [];
  @override
  void dispose() {
    // _controller.dispose();
   listImage = [];
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.amber,
        // title: Text(""),
      ),
      body: Container(
        height: MediaQuery.of(context).size.height,
        color: Colors.amber[50],
        child: FutureBuilder(
            future: getData(),
            builder: (context, AsyncSnapshot snapshot) {
              if (snapshot.connectionState == ConnectionState.waiting) {
                Center(child: CircularProgressIndicator(color: Colors.black));
              } else if (snapshot.hasData) {
                listImage = [];
                List<String> listOfKeys =snapshot.data.keys.toList();
                listOfKeys.removeAt(0); 
                print(listOfKeys);
                print('kkkkkkkkkkkk');
                
                listOfKeys.forEach((element) {
                  listImage.add(Center(
                    child: Text(element),
                  ));
                  for (int i = 0; i <  snapshot.data[element].length; i++) {
                    print(snapshot.data[element][i]);
                    listImage.add(imageBuilder(snapshot.data[element][i]));
                  }
                  
                });
                return ListView(
                  children:listImage,
                
                );
              
              } else if (snapshot.hasError) {
                return Center(
                  child: Row(
                    children: [Text('Error with get data'), Icon(Icons.flag)],
                  ),
                );
              }
              return Container();
            }),
      ),
    );
  }

  Future<dynamic> getData() async {
    Dio dio = Dio();
    final prefs = await SharedPreferences.getInstance();
    String userid = prefs.getString('USERID')!;
    var response =
        await dio.get(Url.OUTPUTSECOND + '?USERID=$userid');

    return response.data;
  }

  Widget imageBuilder(String url) {
    return SizedBox(height: MediaQuery.of(context).size.height/4,child: Image.network('${Url.URL}/$url'));
  }
}
