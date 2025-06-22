import 'package:flutter/material.dart';

class BarScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Bar')),
      body: Center(child: Text('Nur Getränke-Bestellungen anzeigen')),
    );
  }
}
