.. _ug_nrf54h20_suit_push:

How to push SUIT payloads to multiple partitions
################################################

.. contents::
   :local:
   :depth: 2

In the Software Updates for Internet of Things (SUIT), it is possible to push certain payloads separately from the SUIT envelope.
The envelope can than find them in the device and use them as part of the firmware upgrade process.

In Nordic Semiconductor's implementation, this functionality is provide by a mechanism called the DFU cache partitions.

This guide explains how the DFU cache partitions work, and how to configure the build system and SUIT manifests to use them for pushing detached payloads.


Reasons to push images separately from the SUIT envelope
********************************************************

Pushing images separately from the SUIT envelope can be useful in the following scenarios:

* Pushing part of the image to an external memory chip.

* Pushing parts of the update package to non-adjacent memory areas, separated by other data.

* Reducing the amount of data that needs to be resent in case of communication failure to continue the update.

* Pushing parts of the image through different communication channels.

DFU Cache Partitions
********************

The payloads pushed to the device must be placed in so called “DFU cache partitions”, numbered 0..n.
The DFU cache partitions hold data in the format of a CBOR map, in which the keys are URI strings and the values are binary images.

When the Secure Domain processes the manifest and encounters a “fetch” directive it first checks if a given URI is present in its “integrated payloads” section.
If it is not, it goes through all the DFU cache partitions defined in the device.
If the given URI is found as a map key, the binary data stored in the value field corresponding to that URI is fetched.

The DFU cache partition 0 is always present in the device.
It takes all of the space from the dfu_partition which is not occupied by the envelope.
This partition has a limitation - it can only be used after storing the SUIT envelope.

The DFU cache partitions 1…n are defined in the device tree, by using the dfu_cache_partition_x  node name, where x is the partition number.
The partitions can be placed both in the internal MRAM as well as in the external flash.

Extracting images
*********************************************************

The :ref:`nrf54h_suit_sample` sample uses the SMP protocol for uploading new envelopes and is by default configured to use the push model for firmware upgrades.
To reconfigure the sample to allow for pushing images into DFU cache partitions, complete the following steps:

1. Enable the :kconfig:option:`CONFIG_SUIT_DFU_CANDIDATE_PROCESSING_PUSH_TO_CACHE` Kconfig option.
   This enables the writing to the DFU cache partitions.
   Alternatively, you can enable the :kconfig:option:`CONFIG_SUIT_DFU_CANDIDATE_PROCESSING_FULL` option to enable the SUIT envelope processing in the application firmware.
   This will enable a superset of options enabled by :kconfig:option:`CONFIG_SUIT_DFU_CANDIDATE_PROCESSING_PUSH_TO_CACHE`, but will occupy more memory.

#. If you intend to use any other cache partition then 0, add the DFU cache partition in the appropriate memory area in the device tree overlay:

   .. code-block:: dts

		dfu_cache_partition_x: partition@<offset> {
			reg = <<offset> DT_SIZE_K(<size>)>;
		};

   Where ``x`` is the partition number, ``<offset>`` is the offset inside the memory area, and ``<size>`` is the size of the cache partition.

   For example, you could add the cache partition 1 with the size of 1024 kilobytes in the external flash at an offset of 0 by adding:

   .. code-block:: dts

      &mx25uw63 {
         status = "okay";
         partitions {
            compatible = "fixed-partitions";
            #address-cells = <1>;
            #size-cells = <1>;

            dfu_cache_partition_1: partition@0 {
               reg = <0x0 DT_SIZE_K(1024)>;
            };
         };
      };

#. For each of the images you want to push separately to the device:

   * Enable the :kconfig:option:`CONFIG_SUIT_DFU_CACHE_EXTRACT_IMAGE` option
   * (Optionally) modify :kconfig:option:`CONFIG_SUIT_DFU_CACHE_EXTRACT_IMAGE_PARTITION` to select to which partition the image will be pushed (default is 1).
   * (Optionally) modify the :kconfig:option:`CONFIG_SUIT_DFU_CACHE_EXTRACT_IMAGE_URI` to modify the URI used as key for the given image in the DFU cache.

#. Ensure that the uri used by ``suit-payload-fetch`` sequence to fetch a given image matches the :kconfig:option:`CONFIG_SUIT_DFU_CACHE_EXTRACT_IMAGE_URI`.
   Note this is done by default if using the provided Nordic manifest templates.
   <TODO>: do that also for the recovery images.
   For the application image URI this can be done by (assuming the target name "application" for the image):

   .. code-block:: yaml
     - suit-directive-override-parameters:
        suit-parameter-uri: '{{ application['config']['CONFIG_SUIT_DFU_CACHE_EXTRACT_IMAGE_URI'] }}'
     - suit-directive-fetch:
       - suit-send-record-failure

#. Ensure that the envelope does integrate the given image inside the envelope integrated payloads section
   This will be ensured by default if using the provided default SUIT envelope templates.


TODO: Pushing - here or in SMP transfer sample.
******************************
