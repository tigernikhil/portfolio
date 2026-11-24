// Define input and output interfaces
interface InputData {
  rows: any[];
  schema: { [key: string]: string };
}

interface OutputData {
  rows: any[];
  summary: { [key: string]: any };
}

// Core processing function
async function processor(input: InputData): Promise<OutputData> {
  try {
    // Filter data
    const filteredRows = input.rows.filter(row => row.status === 'active');

    // Transform data
    const transformedRows = filteredRows.map(row => ({
      id: row.id,
      name: row.name.toUpperCase(),
      value: row.value * 2
    }));

    // Aggregate data
    const summary = transformedRows.reduce((acc, row) => {
      acc.total += row.value;
      return acc;
    }, { total: 0 });

    // Export data
    return {
      rows: transformedRows,
      summary: summary
    };
  } catch (error) {
    throw new Error(`Error processing data: ${error.message}`);
  }
}

// Export interfaces and function
export { InputData, OutputData, processor };
