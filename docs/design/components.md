# UI Components Design

## Button
- **Purpose**: A button is a clickable element that triggers an action.
- **Usage**: Used in various parts of the UI to initiate actions such as submitting forms, navigating to other pages, or triggering API calls.
- **Attributes**:
  - `type`: Specifies the button type (e.g., `primary`, `secondary`, `danger`, `link`).
  - `size`: Specifies the button size (e.g., `small`, `medium`, `large`).
  - `icon`: Adds an icon to the button for better context.
  - `loading`: A boolean to indicate if the button is in the process of loading.
  - `disabled`: A boolean to disable the button.
  - `onClick`: A function to be called when the button is clicked.

## ToolCard
- **Purpose**: A ToolCard is a container for displaying information and actions related to a specific tool.
- **Usage**: Used in the UI to provide quick access to tools and their functionalities.
- **Attributes**:
  - `title`: The title of the ToolCard.
  - `description`: A brief description of the tool.
  - `icon`: An icon representing the tool.
  - `actions`: A list of actions that can be performed on the tool.
  - `tool`: The actual tool object that the ToolCard represents.

## ToolExecutionPanel
- **Purpose**: A ToolExecutionPanel is a container for executing actions related to a tool.
- **Usage**: Used in the UI to provide a panel for executing actions related to a specific tool.
- **Attributes**:
  - `tool`: The tool for which the actions are being executed.
  - `actions`: A list of actions that can be executed on the tool.
  - `loading`: A boolean to indicate if the panel is in the process of loading.
  - `error`: A boolean to indicate if there is an error in executing the actions.
  - `onAction`: A function to be called when an action is executed.

## StatCard
- **Purpose**: A StatCard is a container for displaying statistics related to a specific entity.
- **Usage**: Used in the UI to provide quick access to statistics related to a specific entity.
- **Attributes**:
  - `entity`: The entity for which the statistics are being displayed.
  - `stats`: A list of statistics related to the entity.
  - `loading`: A boolean to indicate if the card is in the process of loading.
  - `error`: A boolean to indicate if there is an error in fetching the statistics.

## DataTable
- **Purpose**: A DataTable is a container for displaying tabular data.
- **Usage**: Used in the UI to provide a grid view of data.
- **Attributes**:
  - `data`: The data to be displayed in the table.
  - `columns`: The columns of the table.
  - `loading`: A boolean to indicate if the table is in the process of loading.
  - `error`: A boolean to indicate if there is an error in fetching the data.
  - `onRowClick`: A function to be called when a row is clicked.

## Modal
- **Purpose**: A Modal is a dialog box that appears on top of the current UI.
- **Usage**: Used in the UI to provide a way to display information or perform actions in a non-intrusive manner.
- **Attributes**:
  - `title`: The title of the modal.
  - `content`: The content of the modal.
  - `actions`: A list of actions that can be performed in the modal.
  - `loading`: A boolean to indicate if the modal is in the process of loading.
  - `error`: A boolean to indicate if there is an error in displaying the modal.

## Dialog
- **Purpose**: A Dialog is a dialog box that appears on top of the current UI.
- **Usage**: Used in the UI to provide a way to display information or perform actions in a non-intrusive manner.
- **Attributes**:
  - `title`: The title of the dialog.
  - `content`: The content of the dialog.
  - `actions`: A list of actions that can be performed in the dialog.
  - `loading`: A boolean to indicate if the dialog is in the process of loading.
  - `error`: A boolean to indicate if there is an error in displaying the dialog.
