import { ToolManifestSchema, ToolManifest } from '@platform/contracts';
import { ManifestValidationError } from './errors';

function validateManifest(manifest: unknown): ToolManifest {
    const result = ToolManifestSchema.validate(manifest);
    if (result.error) {
        throw new ManifestValidationError(result.error.message);
    }
    return result.value;
}

function validateInput(schema: any, input: unknown): any {
    const result = schema.validate(input);
    if (result.error) {
        throw new Error(result.error.message);
    }
    return result.value;
}

function validateOutput(schema: any, output: unknown): any {
    const result = schema.validate(output);
    if (result.error) {
        throw new Error(result.error.message);
    }
    return result.value;
}

export { validateManifest, validateInput, validateOutput };
