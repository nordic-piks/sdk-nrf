.. _applications:

Applications
############

The |NCS| provides a set of example applications that show how to implement typical user scenarios using Nordic Semiconductor devices.
Applications typically include a fully integrated software stack and can serve as a starting point for developing your product.
They use interface drivers and libraries from the |NCS| and its set of repositories to implement a specific use case, while :ref:`samples` showcase a single feature or library.

Some applications target custom hardware designed for a specific use case.
You can also run them on different hardware like a generic development kit, but with limited functionality.

If you want to list applications available for one or more specific boards, `use the nRF Connect for Visual Studio Code extension to filter them <Browse samples_>`_.

.. toctree::
   :maxdepth: 1
   :glob:
   :caption: Subpages:

   ../../applications/connectivity_bridge/README
   ../../applications/ipc_radio/README
   ../../applications/matter_bridge/README
   ../../applications/nrf5340_audio/index
   ../../applications/nrf_desktop/README
   ../../applications/machine_learning/README
   ../../applications/hpf/hpf
   ../../applications/serial_lte_modem/README
   ../../applications/matter_weather_station/README

Applications are also available through the `nRF Connect SDK Add-ons`_, a curated collection of supplementary |NCS| components.
The `Asset Tracker Template <Asset Tracker Template_>`_ is a Nordic-specific application add-on, on which you can base your application.
