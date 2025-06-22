import 'package:flutter/material.dart';

class KitchenScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Küche')),
      body: Center(child: Text('Nur Essens-Bestellungen anzeigen')),
    );
  }
}
