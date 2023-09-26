import React from "react";
import { View,Text, Image, StyleSheet } from "react-native";
import Logo from "../../../assets/images/logo-app.png"

const SignInScreen = () =>{
    return(
        <View style={styles.root}>
            <Image source={Logo} style={styles.logo} resizeMode="contain" />
        </View>
    )
}

const styles = StyleSheet.create({
    root:{
        alignItems: "center",
        padding: 80,
    },
    logo: {
        width: "70%",
        maxWidth: 300,
        maxHeight: 200,
    }
})


export default SignInScreen