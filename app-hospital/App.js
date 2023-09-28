import React from "react";
import { SafeAreaView, StyleSheet } from "react-native";
import SignInScreen from "./src/screens/SingInScreen/SignInScreen";
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";

export default function App() {
    return (
        <NavigationContainer>
            <Stack.Navigator>
                <SafeAreaView style={styles.root}>
                    <Stack.Screen name="Login" component={LoginScreen} />
                    <Stack.Screen name="Home" component={HomeScreen} />
                    <SignInScreen />
                </SafeAreaView>
            </Stack.Navigator>
        </NavigationContainer>
    );
}

const styles = StyleSheet.create({
    root: {
        flex: 1,
        backgroundColor: "lightblue",
    },
});
