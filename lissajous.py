"""A streamlit app that allows to draw lissajous curves.

The app has two sliders to control the frequency of the curves.
"""

from typing import Any
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Set up the page
st.title("Lissajous curves")
st.markdown(
    """
    This app allows to draw lissajous curves. The app has two sliders to control
    the frequency of the curves.
    """
)

# Set up the sliders
st.sidebar.markdown("## Frequency")
a = st.sidebar.slider("a", 1.0, 10.0, 0.5)
b = st.sidebar.slider("b", 1.0, 10.0, 0.5)

# Draw the curves
t: np.ndarray[Any, np.dtype[np.floating]] = np.linspace(0, 4 * np.pi, 1000)
x = np.sin(a * t)
y = np.sin(b * t)
c = np.cos(a * t)
fig, ax = plt.subplots()
ax.plot(x, y, "r-", c, y, "b-")
# remove axes
ax.axis("off")
st.pyplot(fig)


def fig_to_base64(fig):
    """Convert a matplotlib figure to base64."""
    import io
    import base64

    buf = io.BytesIO()
    fig.savefig(buf, format="pdf", bbox_inches="tight")
    data = base64.b64encode(buf.getbuffer()).decode("utf8")
    return data


# Save the page
st.markdown("## Download the page")
st.markdown(
    """
    The page can be downloaded as a PDF file. The file can be opened with a
    PDF viewer such as Adobe Acrobat Reader.
    """
)
st.markdown(
    """
    <a href="data:application/pdf;base64,{}" download="lissajous.pdf">
    <button class="css-1aumxhk">Download PDF</button>
    </a>
    """.format(
        fig_to_base64(fig)
    ),
    unsafe_allow_html=True,
)
