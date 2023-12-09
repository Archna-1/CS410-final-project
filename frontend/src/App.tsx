import {
  Box,
  Button,
  Input,
  ChakraProvider,
  Heading,
  FormControl,
} from "@chakra-ui/react";

import axios from "axios";
import { useState } from "react";

function App() {
  const [summary, setSummary] = useState<String>();

  const onSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    const input = (document.getElementById("input") as HTMLInputElement)?.value;
    let res = await axios.post(
      "http://localhost:5001/get-remote-text",
      {
        url: input,
      },
      {
        headers: {
          "Content-Type": "application/json",
        },
      }
    );

    setSummary(res.data.text);
  };

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
        <form onSubmit={(e) => onSubmit(e)}>
          <Input id="input" mb="5px" placeholder="Enter URL here"></Input>
          <Button mb="10px" type="submit">
            Get Summary
          </Button>
        </form>
        {summary && (
          <>
            <Heading mb="5px" fontSize="2em">
              Summary
            </Heading>
            <Box
              mb="5px"
              overflowY="auto"
              h="120px"
              border="2px lightgray solid"
              borderRadius="5px"
            >
              {summary}
            </Box>
          </>
        )}
      </Box>
    </ChakraProvider>
  );
}

export default App;
