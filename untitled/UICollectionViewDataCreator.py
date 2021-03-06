import json
import os
dict_temp = {
    "init": "UICollectionViewDelegate,UICollectionViewDataSource\nUICollectionViewFlowLayout* flowLayout = [[UICollectionViewFlowLayoutalloc]init];\nflowLayout.minimumLineSpacing = 0;\nflowLayout.minimumInteritemSpacing = 0;\nflowLayout.itemSize=CGSizeMake(itemWidth,itemHeight);\nflowLayout.scrollDirection = UICollectionViewScrollDirectionHorizontal;\n\nUICollectionView*WHYName = [[UICollectionViewalloc]initWithFrame:CGRectMake(<#Content#>)collectionViewLayout:flowLayout];\nWHYName.bounces = NO;\nWHYName.delegate = self;\nWHYName.dataSource = self;\nWHYName.showsVerticalScrollIndicator = NO;\nWHYName.showsHorizontalScrollIndicator = NO;",
    "frame": "WHYName.frame = CGRectMake(<#CGFloat x#>, <#CGFloat y#>, <#CGFloat width#>, <#CGFloat height#>);",
    "backgroundColor": "WHYName.backgroundColor = UIColor.whiteColor;",
    "registerClass": "NSString* const CellIdentifier = @\"CellIdentifier\";\n[WHYName registerClass:[<#ELInteractiveListTableViewCell#> class] forCellReuseIdentifier:CellIdentifier];",
    "addSubView": "[<#self#> addSubview:WHYName];",
    "masonry": "[WHYName mas_makeConstraints:^(MASConstraintMaker *make) {\n}];",
    "sectionNum": "- (NSInteger)numberOfSectionsInCollectionView:(UICollectionView*)collectionView{\nreturn_topSearchComponent.render.horizontal;\n}\n",
    "rowNum": "- (NSInteger)collectionView:(UICollectionView *)collectionView numberOfItemsInSection:(NSInteger)section\n{\nreturn _topSearchComponent.render.vertical;\n}",
    "ItemSize": "- (CGSize)collectionView:(UICollectionView *)collectionView layout:(UICollectionViewLayout*)collectionViewLayout sizeForItemAtIndexPath:(NSIndexPath *)indexPath\n{\nreturn CGSizeMake(itemWidth, itemHeight);\n}",
    "cellView": "- (UICollectionViewCell *)collectionView:(UICollectionView *)collectionView cellForItemAtIndexPath:(NSIndexPath *)indexPath\n{\nQSTopSearchCollectionViewCell *cell = [collectionView dequeueReusableCellWithReuseIdentifier:CellIdentifier forIndexPath:indexPath];\nreturn cell;\n}\n",
    "SectionInset": "- (UIEdgeInsets)collectionView:(UICollectionView *)collectionView layout:(UICollectionViewLayout *)collectionViewLayout insetForSectionAtIndex:(NSInteger)section\n{\nreturn UIEdgeInsetsMake(18, 10, 18, 0);\n}",
    "selectCell": "- (void)collectionView:(UICollectionView *)collectionView didSelectItemAtIndexPath:(NSIndexPath *)indexPath\n{\n}",
}

file = open("UIFilePath.txt", 'r')
dict = json.loads(file.read())
myFile = dict["UICollectionView"]

if os.path.exists(myFile):
    os.remove(myFile)
file = open(myFile, 'w')
file.write(json.dumps(dict_temp))
# 注意关闭文件
file.close()

file = open(myFile, 'r')
dict = json.loads(file.read())
print(dict)
print(dict["init"])
# 注意关闭文件
file.close()