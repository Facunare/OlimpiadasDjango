import React from "react";
import { View, Text, Image, StyleSheet } from "react-native";
import Logo from "../../../assets/images/logo-app.png";
import CustomInput from "../../components/CustomsInput/CustomInput";

const SignInScreen = () => {
    return (
        <View style={styles.root}>
            <Image source={Logo} style={styles.logo} resizeMode="contain" />
            <CustomInput />
        </View>
    );
};

const styles = StyleSheet.create({
    root: {
        alignItems: "center",
        paddingTop: 80,
    },
    logo: {
        width: "40%",
        maxWidth: 300,
        maxHeight: 200,
    },
});

export default SignInScreen;
