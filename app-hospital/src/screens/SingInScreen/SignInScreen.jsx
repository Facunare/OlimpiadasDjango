import React, { useState } from "react";
import { View, Text, Image, StyleSheet } from "react-native";
import { useNavigation } from "@react-navigation/native";
import Logo from "../../../assets/images/logo-app.png";
import CustomInput from "../../components/CustomsInput/CustomInput";
import CustomButton from "../../components/CustomsButton/CustomButton";

const SignInScreen = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const navigation = useNavigation();

    const onSignInPressed = () => {
        if (username === "abc" && password === "123") {
            navigation.navigate("Main");
        } else {
            console.warn("Credenciales incorrectas");
        }
    };

    const onForgotPasswordPressed = () => {
        console.warn("Bonto de recuperar");
    };

    return (
        <View style={styles.root}>
            <Image source={Logo} style={styles.logo} resizeMode="contain" />

            <CustomInput
                placeholder="Usuario"
                value={username}
                setValue={setUsername}
            />
            <CustomInput
                placeholder="Contraseña"
                value={password}
                setValue={setPassword}
                secureTextEntry
            />

            <CustomButton text="Iniciar Sesion" onPress={onSignInPressed} />

            <CustomButton
                text="Olvidaste tu contraseña?"
                onPress={onForgotPasswordPressed}
                type="TERTIARY"
            />
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
