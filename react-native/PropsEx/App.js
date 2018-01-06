import React, { Component } from "react";
import { AppRegistry, Text, StyleSheet, View } from "react-native";

class Greeting extends Component {
  render() {
    return <Text>Hello {this.props.name}</Text>;
  }
}

export default class Greetings extends Component {
  render() {
    return (
      <View style={styles.container}>
        <Greeting name="Rexxar" />
        <Greeting name="Jaina" />
        <Greeting name="Valeera" />
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center"
  }
});

AppRegistry.registerComponent("PropsEx", () => Greetings);
