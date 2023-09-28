import { View, Text, TextInput, StyleSheet } from "react-native";
import React from "react";

const CustomInput = ({ value, setValue, placeholder, secureTextEntry }) => {
    return (
        <View style={styles.container}>
            <TextInput
                value={value}
                onChangeText={setValue}
                placeholder={placeholder}
                style={styles.input}
                secureTextEntry={secureTextEntry}
            />
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        backgroundColor: "white",
        width: "90%",
        height: "7%",
        borderColor: "#e8e8e8",
        borderWidth: 3,
        borderRadius: 3,
        paddingHorizontal: 7,
        paddingVertical: 10,
        marginVertical: 5,
    },
    input: {},
});

export default CustomInput;
