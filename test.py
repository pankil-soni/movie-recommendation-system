import streamlit as st

# Add your horizontally scrollable content
horizontal_content = """
<div style="overflow-x: scroll;">
    <p>This is a horizontally scrollable element.</p>
    <p>You can add any content here that you want to scroll horizontally.</p>
    <p>For example, a wide table or a long line of text.</p>
    <table>
        <tr>
            <th>Header 1</th>
            <th>Header 2</th>
            <th>Header 3</th>
            <th>Header 4</th>
            <th>Header 5</th>
            <th>Header 6</th>
        </tr>
        <tr>
            <td>Data 1</td>
            <td>Data 2</td>
            <td>Data 3</td>
            <td>Data 4</td>
            <td>Data 5</td>
            <td>Data 6</td>
        </tr>
    </table>
</div>
"""

# Display the horizontally scrollable element
st.write(horizontal_content, unsafe_allow_html=True)
