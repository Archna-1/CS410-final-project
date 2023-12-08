import {
  Box,
  Button,
  Flex,
  Input,
  Text,
  ChakraProvider,
  Heading,
} from "@chakra-ui/react";

function App() {
  let res = "summary"; // add api call here

  return (
    <ChakraProvider>
      <Box
        margin="auto"
        alignItems="center"
        justifyContent="center"
        display="block"
        w="15rem"
        h="auto"
        flexDir="column"
        padding="5%"
        borderRadius="10px"
      >
        <Heading mb="5px" fontSize="2.2em">
          CS410 Article Summarizer
        </Heading>
        <Input mb="5px" placeholder="Enter URL here"></Input>
        <Button mb="10px">Get Summary</Button>
        <Heading mb="5px" fontSize="2em">
          Summary
        </Heading>
        {res && (
          <Box
            mb="5px"
            overflowY="auto"
            h="120px"
            border="2px lightgray solid"
            borderRadius="5px"
          >
            {res}
          </Box>
        )}
      </Box>
    </ChakraProvider>
  );
}

export default App;
