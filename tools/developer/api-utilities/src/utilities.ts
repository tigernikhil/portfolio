// developer.api-utilities.ts

import axios from 'axios';
import jwtDecode from 'jwt-decode';
import Ajv from 'ajv';

// Define input and output interfaces for each utility

// Curl to fetch generator
interface CurlToFetchInput {
  url: string;
  method?: 'GET' | 'POST' | 'PUT' | 'DELETE';
  headers?: { [key: string]: string };
  data?: any;
}

interface CurlToFetchOutput {
  status: number;
  data: any;
  headers: { [key: string]: string };
}

// JWT decoder
interface JwtDecodeInput {
  token: string;
}

interface JwtDecodeOutput {
  decoded: any;
}

// Header inspector
interface HeaderInspectorInput {
  headers: { [key: string]: string };
  key: string;
}

interface HeaderInspectorOutput {
  value: string | undefined;
}

// JSON schema validator
interface JsonSchemaValidatorInput {
  data: any;
  schema: any;
}

interface JsonSchemaValidatorOutput {
  valid: boolean;
  errors?: string[];
}

// Core processing function
export async function utilities(input: any): Promise<any> {
  try {
    if ('url' in input) {
      return await curlToFetch(input as CurlToFetchInput);
    } else if ('token' in input) {
      return await jwtDecode(input as JwtDecodeInput);
    } else if ('headers' in input && 'key' in input) {
      return await headerInspector(input as HeaderInspectorInput);
    } else if ('data' in input && 'schema' in input) {
      return await jsonSchemaValidator(input as JsonSchemaValidatorInput);
    } else {
      throw new Error('Invalid input');
    }
  } catch (error) {
    throw new Error(`Error in API Developer Utilities: ${error.message}`);
  }
}

// Implementation of each utility

async function curlToFetch(input: CurlToFetchInput): Promise<CurlToFetchOutput> {
  const { url, method = 'GET', headers = {}, data = null } = input;
  const response = await axios({
    url,
    method,
    headers,
    data,
  });
  return {
    status: response.status,
    data: response.data,
    headers: response.headers,
  };
}

function jwtDecode(input: JwtDecodeInput): JwtDecodeOutput {
  const { token } = input;
  return {
    decoded: jwtDecode(token),
  };
}

async function headerInspector(input: HeaderInspectorInput): Promise<HeaderInspectorOutput> {
  const { headers, key } = input;
  return {
    value: headers[key],
  };
}

async function jsonSchemaValidator(input: JsonSchemaValidatorInput): Promise<JsonSchemaValidatorOutput> {
  const { data, schema } = input;
  const ajv = new Ajv();
  const validate = ajv.compile(schema);
  const valid = validate(data);
  if (!valid) {
    return {
      valid: false,
      errors: validate.errors?.map((error: any) => error.message),
    };
  }
  return {
    valid: true,
  };
}
