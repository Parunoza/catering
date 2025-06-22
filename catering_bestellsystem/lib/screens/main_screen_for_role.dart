import 'package:flutter/material.dart';
import 'config.dart';
import 'table_overview.dart';
import 'kitchen_screen.dart';
import 'bar_screen.dart';
import 'admin_screen.dart';

class MainScreenForRole extends StatelessWidget {
  final UserRole role;

  MainScreenForRole({required this.role});

  @override
  Widget build(BuildContext context) {
    switch (role) {
      case UserRole.KELLNER:
        return TableOverviewScreen();
      case UserRole.KUECHE:
        return KitchenScreen();
      case UserRole.BAR:
        return BarScreen();
      case UserRole.ADMIN:
        return AdminScreen();
    }
  }
}
