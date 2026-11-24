import { PDFDocument } from 'pdf-lib';
import { PDFParser } from 'pdf2json';
import { TextItem } from 'pdf2json';

// Define input and output interfaces
interface AnalyzerInput {
  pdfBuffer: Buffer;
}

interface AnalyzerOutput {
  metadata: any;
  headings: string[];
  tables: any[];
  wordFrequency: { [word: string]: number };
}

// Core processing function
export async function analyzer(input: AnalyzerInput): Promise<AnalyzerOutput> {
  try {
    // Parse PDF metadata
    const pdfParser = new PDFParser();
    pdfParser.parseBuffer(input.pdfBuffer);
    const pdfData = await new Promise((resolve, reject) => {
      pdfParser.on('pdfParser_dataReady', (data) => resolve(data));
      pdfParser.on('pdfParser_dataError', (error) => reject(error));
    });

    // Extract metadata
    const metadata = pdfData.info;

    // Extract headings and tables
    const headings: string[] = [];
    const tables: any[] = [];
    const textItems: TextItem[] = pdfData.texts;
    for (const item of textItems) {
      if (item.str.includes('\n')) {
        tables.push(item.str);
      } else if (item.size > 12) {
        headings.push(item.str);
      }
    }

    // Count word frequency
    const wordFrequency: { [word: string]: number } = {};
    for (const item of textItems) {
      const words = item.str.split(/\s+/);
      for (const word of words) {
        if (wordFrequency[word]) {
          wordFrequency[word]++;
        } else {
          wordFrequency[word] = 1;
        }
      }
    }

    return {
      metadata,
      headings,
      tables,
      wordFrequency,
    };
  } catch (error) {
    throw new Error(`Error analyzing PDF: ${error.message}`);
  }
}
