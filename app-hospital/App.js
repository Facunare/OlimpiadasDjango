import React from "react";
import { SafeAreaView, StyleSheet } from "react-native";
import SignInScreen from "./src/screens/SingInScreen/SignInScreen.jsx"; 
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";
import Main from "./src/navigation/Main.jsx"

const Stack = createStackNavigator();

export default function App() {
    return (
        <NavigationContainer>
            <Stack.Navigator>
                <Stack.Screen name="Login" component={SignInScreen} />
                <Stack.Screen name="Main" component={Main} />
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
