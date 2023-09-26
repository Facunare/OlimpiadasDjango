import { View, Text, TextInput, StyleSheet } from "react-native";
import React from "react";

const CustomInput = () => {
    return (
        <View style={styles.container}>
            <TextInput placeholder="placeholder" style={styles.input} />
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        backgroundColor: "white",
        width: "90%",
        height: "5%",
        borderColor: "#e8e8e8",
        borderWidth: 1,
        borderRadius: 5,
    },
    input: {},
});

export default CustomInput;
