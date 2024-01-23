import azure.ai.vision as visionsdk

key = "90ec7478c6994a438a9de30cb245a810"
endpoint = "https://cs1-37127687.cognitiveservices.azure.com/"

def AnalyzeImage(endpoint: str, key: str) -> None:
    # Point 1: Set up the Azure Vision client
    service_options = visionsdk.VisionServiceOptions(endpoint, key)

    # Point 2: Specify the image file on disk to analyze. text.jpg is a good example to show most features
    vision_source = visionsdk.VisionSource(filename=r"text.jpg")

    # Point 3: Specify the features for analysis (OBJECTS, TAGS, PEOPLE, TEXT)
    analysis_options = visionsdk.ImageAnalysisOptions()
    analysis_options.features = (
        visionsdk.ImageAnalysisFeature.OBJECTS |
        visionsdk.ImageAnalysisFeature.TAGS |
        visionsdk.ImageAnalysisFeature.PEOPLE |
        visionsdk.ImageAnalysisFeature.TEXT
    )

    # Point 4: Create an ImageAnalyzer instance
    image_analyzer = visionsdk.ImageAnalyzer(service_options, vision_source, analysis_options)
    print("Please wait for image analysis results...")

    # Point 5: Analyze the image
    result = image_analyzer.analyze()

    # Checks result.
    if result.reason == visionsdk.ImageAnalysisResultReason.ANALYZED:
        # Point 6: Process detected objects
        if result.objects is not None:
            print("Objects:")
            for object in result.objects:
                print(f"   {object.name}")

        # Point 7: Process detected tags
        if result.tags is not None:
            print("Tags:")
            for tag in result.tags:
                print(f"   {tag.name} with confidence {tag.confidence}")

        # Point 8: Process detected people
        if result.people is not None:
            print("People:")
            for person in result.people:
                print(f"   {person.name}")

        # Point 9: Process detected text
        if result.text is not None:
            print("Text:")
            for line in result.text.lines:
                print(f"   {line.content}")
    else:
        # Point 10: Handle analysis failure
        error_details = visionsdk.ImageAnalysisErrorDetails.from_result(result)
        print("Analysis failed.")
        print("   Error reason: {}".format(error_details.reason))
        print("   Error code: {}".format(error_details.error_code))
        print("   Error message: {}".format(error_details.message))
        print("Did you set the computer vision endpoint and key?")

# Point 11: Call the AnalyzeImage function with the specified endpoint and key
AnalyzeImage(endpoint, key)
