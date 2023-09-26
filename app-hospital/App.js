import React from "react";
import { SafeAreaView, StyleSheet,Text } from "react-native";
import SignInScreen from "./src/screens/SingInScreen/SignInScreen"; 

export default function App () {
  return (
    <SafeAreaView style={styles.root}>
      <SignInScreen/>
    </SafeAreaView>
  )
}



const styles = StyleSheet.create({
  root: {
    flex: 1,
  },
})